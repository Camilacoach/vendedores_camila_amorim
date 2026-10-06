# -*- coding: utf-8 -*-
"""
Replicação simplificada de Krueger (1999),
"Experimental Estimates of Education Production Functions" - Projeto STAR.

Parte A: regressões MQO para o jardim de infância (estilo Tabela V do artigo).
Parte B: 4 gráficos, mostrados na tela e salvos como PNG.

Requisitos: pip install pandas statsmodels matplotlib numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# ---------------------------------------------------------------
# 1. Carregar os dados (mesma base do pacote AER do R)
# ---------------------------------------------------------------
url = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/AER/STAR.csv"
star = pd.read_csv(url)

# Mantém só os alunos que estavam no experimento no jardim de infância
d = star[star["stark"].notna()].copy()

# ---------------------------------------------------------------
# 2. Variável dependente: nota em percentis (como Krueger)
#    Cada nota vira um percentil em relação à distribuição dos alunos
#    de turmas REGULARES (com e sem auxiliar). Depois tira a média
#    entre leitura e matemática.
# ---------------------------------------------------------------
def percentil_vs_regular(nota, grupo_ref):
    ref = nota[grupo_ref].dropna().sort_values().values
    return nota.apply(
        lambda x: (ref <= x).mean() * 100 if pd.notna(x) else float("nan")
    )

regular = d["stark"].isin(["regular", "regular+aide"])
d["pct_read"] = percentil_vs_regular(d["readk"], regular)
d["pct_math"] = percentil_vs_regular(d["mathk"], regular)
d["nota"] = d[["pct_read", "pct_math"]].mean(axis=1, skipna=False)

# ---------------------------------------------------------------
# 3. Variáveis explicativas
# ---------------------------------------------------------------
d["pequena"] = (d["stark"] == "small").astype(int)          # turma pequena
d["auxiliar"] = (d["stark"] == "regular+aide").astype(int)  # turma regular c/ auxiliar
d["branco_asiat"] = d["ethnicity"].isin(["cauc", "asian"]).astype(int)
d["menina"] = (d["gender"] == "female").astype(int)
d["merenda"] = (d["lunchk"] == "free").astype(int)          # proxy de baixa renda
d["prof_branco"] = (d["tethnicityk"] == "cauc").astype(int)
d["prof_exp"] = d["experiencek"]
d["prof_mestrado"] = d["degreek"].isin(["master", "master+", "specialist"]).astype(int)
d["escola"] = d["schoolidk"].astype(int).astype(str)

# Usa a mesma amostra em todas as colunas
cols = ["nota", "pequena", "auxiliar", "branco_asiat", "menina", "merenda",
        "prof_branco", "prof_exp", "prof_mestrado", "escola"]
d = d.dropna(subset=cols)

# ---------------------------------------------------------------
# 4. Regressões (erros-padrão robustos, agrupados por escola)
# ---------------------------------------------------------------
modelos = {
    "(1) Só tratamento": "nota ~ pequena + auxiliar",
    "(2) + EF escola":   "nota ~ pequena + auxiliar + C(escola)",
    "(3) + aluno":       "nota ~ pequena + auxiliar + branco_asiat + menina + merenda + C(escola)",
    "(4) + professor":   "nota ~ pequena + auxiliar + branco_asiat + menina + merenda"
                         " + prof_branco + prof_exp + prof_mestrado + C(escola)",
}

vars_mostrar = ["pequena", "auxiliar", "branco_asiat", "menina", "merenda",
                "prof_branco", "prof_exp", "prof_mestrado"]

tabela = pd.DataFrame(index=vars_mostrar + ["R²", "N"])
for nome, formula in modelos.items():
    res = smf.ols(formula, data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["escola"]}
    )
    col = {}
    for v in vars_mostrar:
        if v in res.params:
            col[v] = f"{res.params[v]:.2f} ({res.bse[v]:.2f})"
        else:
            col[v] = ""
    col["R²"] = f"{res.rsquared:.3f}"
    col["N"] = f"{int(res.nobs)}"
    tabela[nome] = pd.Series(col)

pd.set_option("display.width", 200)
print("\nEfeito do tamanho da turma na nota (percentil) - Jardim de infância")
print("Coeficiente (erro-padrão agrupado por escola)\n")
print(tabela.to_string())

# ===============================================================
# PARTE B - GRÁFICOS
# ===============================================================
d["turma"] = d["stark"].map({"small": "Pequena", "regular": "Regular",
                             "regular+aide": "Regular + auxiliar"})

plt.rcParams.update({
    "figure.dpi": 120, "savefig.dpi": 200, "font.size": 11,
    "axes.spines.top": False, "axes.spines.right": False,
})
CORES = {"Pequena": "#2a7ab9", "Regular": "#9a9a9a", "Regular + auxiliar": "#e0913a"}
ordem = ["Pequena", "Regular", "Regular + auxiliar"]

# ---------------------------------------------------------------
# Figura 1 - Distribuição das notas por tipo de turma
# (parecida com a Figura I do artigo)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.8))
grade = np.linspace(0, 100, 201)
for t in ordem:
    x = d.loc[d["turma"] == t, "nota"].values
    # densidade por kernel gaussiano simples (sem depender do scipy)
    h = 1.06 * x.std() * len(x) ** (-1 / 5)
    dens = np.exp(-0.5 * ((grade[:, None] - x[None, :]) / h) ** 2).sum(1)
    dens /= len(x) * h * np.sqrt(2 * np.pi)
    ax.plot(grade, dens, color=CORES[t], lw=2.2, label=f"{t} (n={len(x)})")
ax.set_xlabel("Nota média (percentil)")
ax.set_ylabel("Densidade")
ax.set_title("Distribuição das notas no jardim de infância, por tipo de turma")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("fig1_distribuicao_notas.png")
plt.show()

# ---------------------------------------------------------------
# Figura 2 - Nota média por tipo de turma, com IC de 95%
# ---------------------------------------------------------------
resumo = d.groupby("turma")["nota"].agg(["mean", "std", "count"]).loc[ordem]
resumo["ic"] = 1.96 * resumo["std"] / np.sqrt(resumo["count"])

fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.bar(ordem, resumo["mean"], yerr=resumo["ic"], capsize=6,
       color=[CORES[t] for t in ordem], width=0.6)
for i, m in enumerate(resumo["mean"]):
    ax.text(i, m + resumo["ic"].iloc[i] + 0.8, f"{m:.1f}", ha="center")
ax.set_ylim(0, resumo["mean"].max() + 8)
ax.set_ylabel("Nota média (percentil)")
ax.set_title("Nota média por tipo de turma (IC de 95%)")
fig.tight_layout()
fig.savefig("fig2_media_por_turma.png")
plt.show()

# ---------------------------------------------------------------
# Figura 3 - Coeficiente de "turma pequena" nos 4 modelos
# ---------------------------------------------------------------
coefs = []
for nome, f in modelos.items():
    r = smf.ols(f, data=d).fit(cov_type="cluster", cov_kwds={"groups": d["escola"]})
    coefs.append((nome, r.params["pequena"], r.bse["pequena"]))

fig, ax = plt.subplots(figsize=(7.5, 4))
y = np.arange(len(coefs))[::-1]
for yi, (nome, b, se) in zip(y, coefs):
    ax.errorbar(b, yi, xerr=1.96 * se, fmt="o", color=CORES["Pequena"],
                capsize=5, ms=8, lw=2)
    ax.text(b, yi + 0.18, f"{b:.2f}", ha="center")
ax.axvline(0, color="black", lw=0.8, ls="--")
ax.set_yticks(y)
ax.set_ylim(-0.5, len(y) - 0.3)
ax.set_yticklabels([c[0] for c in coefs])
ax.set_xlabel("Efeito de turma pequena (pontos percentis) com IC de 95%")
ax.set_title("O efeito é estável quando adicionamos controles")
fig.tight_layout()
fig.savefig("fig3_coeficientes_modelos.png")
plt.show()

# ---------------------------------------------------------------
# Figura 4 - Efeito heterogêneo: turma pequena por subgrupo
# (o artigo destaca efeito maior para negros e alunos de baixa renda)
# ---------------------------------------------------------------
subgrupos = {
    "Merenda gratuita": d["merenda"] == 1,
    "Sem merenda gratuita": d["merenda"] == 0,
    "Alunos negros": d["ethnicity"] == "afam",
    "Alunos brancos/asiáticos": d["branco_asiat"] == 1,
}
res_sub = []
for nome, filtro in subgrupos.items():
    s = d[filtro]
    r = smf.ols("nota ~ pequena + auxiliar + menina + C(escola)", data=s).fit(
        cov_type="cluster", cov_kwds={"groups": s["escola"]})
    res_sub.append((nome, r.params["pequena"], r.bse["pequena"], len(s)))

fig, ax = plt.subplots(figsize=(7.5, 4))
y = np.arange(len(res_sub))[::-1]
cores_sub = ["#2a7ab9", "#8fb8db", "#2a7ab9", "#8fb8db"]
for yi, (nome, b, se, n), c in zip(y, res_sub, cores_sub):
    ax.errorbar(b, yi, xerr=1.96 * se, fmt="o", color=c, capsize=5, ms=8, lw=2)
    ax.text(b, yi + 0.18, f"{b:.2f}", ha="center")
ax.axvline(0, color="black", lw=0.8, ls="--")
ax.set_yticks(y)
ax.set_ylim(-0.5, len(y) - 0.3)
ax.set_yticklabels([f"{r[0]} (n={r[3]})" for r in res_sub])
ax.set_xlabel("Efeito de turma pequena (pontos percentis) com IC de 95%")
ax.set_title("Efeito de turma pequena por subgrupo")
fig.tight_layout()
fig.savefig("fig4_efeito_por_subgrupo.png")
plt.show()

print("Pronto! Figuras salvas:")
for f in ["fig1_distribuicao_notas.png", "fig2_media_por_turma.png",
          "fig3_coeficientes_modelos.png", "fig4_efeito_por_subgrupo.png"]:
    print("  -", f)