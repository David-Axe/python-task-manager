#EXERCICIO:
#Receba uma lista de nomes (separados por virgula) e:
#Remova espacos extras
#Coloque em formato "Nome Sobrenome"
#Ordene alfabeticamente
#Remova duplicatas
#Mostre a lista final numerada

#ALGORITMO:
#1. Receber nomes separados por vírgula;
#2. Separar os nomes usando split(',');
#3. Para cada nome:
    #4. Remover espaços extras com strip();
    #5. Formatar com title() para "Nome Sobrenome";
#6. Remover duplicatas usando set();
#7. Ordenar alfabeticamente com sorted();
#8. Mostrar a lista numerada;

# =============================================================================
# ORGANIZADOR DE NOMES
# =============================================================================
# Objetivo: Receber uma lista de nomes e organizá-los
# 
# Como usar:
# - Digite nomes separados por vírgula (ex: joão silva, maria santos, joão silva)
# - O programa ira:
#   * Remover espaços extras
#   * Formatar cada nome para "Nome Sobrenome"
#   * Ordenar alfabeticamente
#   * Remover nomes duplicados
#   * Mostrar a lista final numerada
# 
# Resultado: Lista organizada e sem duplicatas
# =============================================================================

#Código:

nomes_input = input("Digite os nomes que deseja listar (por favor, separar por vírgula): ")

nomes_lista = [nome.strip() for nome in nomes_input.split(',')]

nomes_formatados = [nome.title() for nome in nomes_lista]

nomes_unicos = list(set(nomes_formatados))

nomes_ordenados = sorted(nomes_unicos)

print("\nLista organizada:")
for i, nome in enumerate(nomes_ordenados, 1):
    print(f"{i}. {nome}")
