import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#fonte de dados https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=1378939680

gsheets_sisref_id = "1378939680"
gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=' + gsheets_sisref_id

@st.cache_data(ttl=120)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(gsheets_url)

st.sidebar.subheader("Selecione se deseja exibir")
show_dataset = st.sidebar.checkbox("Dados do Dataset")

if show_dataset:
    st.subheader("Conjunto de Dados")
    st.dataframe(data)


#Mostrando a quantidade de refeições
st.subheader("Número de Refeições por periodo")
refeicoes = data['Refeicao'].value_counts()
fig_refeicao, ax_refeicao = plt.subplots()
sns.barplot(x=refeicoes.index,y=refeicoes.values)
ax_refeicao.set_xlabel('Tipo de Refeição')
ax_refeicao.set_ylabel('Número de Estudantes')
for i in ax_refeicao.containers:
    ax_refeicao.bar_label(i,)
st.pyplot(fig_refeicao)

#Mostrando o comparecimento dos alunos
st.subheader("Total de Comparecimento dos Alunos ao marcarem as refeições")
num_comparecimento = data['Compareceu'].value_counts()
fig_curso, ax_curso = plt.subplots()
ax_curso.pie(num_comparecimento.values,labels=num_comparecimento.index,autopct='%1.2f%%')
st.pyplot(fig_curso)

#Maior refeição por datas
st.subheader('Datas que tiveram maior número de Refeições')
num_data = data['Data da Solicitacao'].value_counts()
fig_justificacao, ax_justificacao = plt.subplots()
ax_justificacao.pie(num_data.values,labels=num_data.index,autopct='%1.2f%%',pctdistance=0.8,labeldistance=1.2)
st.pyplot(fig_justificacao)

#Número de Refeições por curso
st.subheader('Dados do número de Refeições dos cursos')
num_if_total = data.groupby('Curso')['Compareceu'].value_counts()
st.dataframe(num_if_total)

st.subheader('Datas que tiveram maior número de Refeições por curso')
num_refeicao_curso = data.groupby('Curso')['Data da Solicitacao'].value_counts()
st.dataframe(num_refeicao_curso)