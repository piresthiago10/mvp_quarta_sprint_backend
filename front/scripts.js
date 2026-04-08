const btnFazerPredicao = document.getElementById('fazer-predicao-btn');
const btnVerResultados = document.getElementById('ver-resultados-btn');
const btnFormVoltar = document.getElementById('inicio-form-btn');
const btnVoltarInicio = document.getElementById('inicio-btn');
const btnFormEnviarResposta = document.getElementById('enviar-resposta-form-btn');
const sectionResultado = document.getElementById('section-resultado');
const sectionDescription = document.getElementById("app-description");
const formSection = document.getElementById("form");
const sectionResultados = document.getElementById("section-resultados");
const btnInicicioResultados = document.getElementById("inicio-resultados-btn");
const modal = document.getElementById("modal-individuo");
const fecharModal = document.getElementById("fechar-modal");

document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector('button[type="button"]');
  const formSection = document.getElementById("form");

  button.addEventListener("click", function () {
    // mostra o formulário
    formSection.style.display = "block";

    // esconde a descrição
    sectionDescription.style.display = "none";
  });
});

// endpoint da API
const API_URL = 'http://127.0.0.1:5000';

// captura o formulário
const form = document.querySelector("#wellness-form");

// função para converter o formulário em JSON
function formToJSON(formElement) {
  const formData = new FormData(formElement);
  const data = {};

  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  return data;
}

// função que chama a API
async function sendPrediction(data) {
  try {
    const response = await fetch(`${API_URL}/individuos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }

    return await response.json();

  } catch (error) {
    console.error("Erro ao consumir API:", error);
    throw error;
  }
}

// fazer um get em /individuo
async function getIndividuos() {
  try {
    const response = await fetch(`${API_URL}/individuos`);
    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Erro ao consumir API:", error);
    throw error;
  }
}

// preencher a tabela com dados de getIndividuos()
async function preencherTabela() {
  try {
    const individuos = await getIndividuos();
    const tbody = document.querySelector("tbody");
    tbody.innerHTML = "";
    individuos.forEach((individuo) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${individuo.id}</td>
        <td>${individuo.name}</td>
        <td>${individuo.cpf}</td>
        <td>${individuo.age}</td>
        <td>${individuo.gender}</td>
        <td>${individuo.outcome}</td>
        <td>
          <a href="#" onclick="pesquisarIndividuo('${individuo.id}')">
            Detalhes
          </a>
          <a href="#" onclick="excluirIndividuo('${individuo.id}')">
            Excluir
          </a>
        </td>
      `;
      tbody.appendChild(row);
    });
  } catch (error) {
    console.error("Erro ao preencher a tabela:", error);
  }
}

async function excluirIndividuo(idIndividuo) {
  try {
    const response = await fetch(`${API_URL}/individuos/${idIndividuo}`, {
      method: "DELETE"
    });
    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }
    await preencherTabela();
  } catch (error) {
    console.error("Erro ao excluir individuo:", error);
  }
}

btnVerResultados.addEventListener("click", async () => {
  await preencherTabela();
  sectionDescription.style.display = "none";
  sectionResultados.style.display = "block";
});

// handler do submit
btnFormEnviarResposta.addEventListener("click", async (event) => {
  event.preventDefault();
  const data = formToJSON(form);
  try {
    const result = await sendPrediction(data);

    console.log("Resposta da API:", result);

    sectionResultado.style.display = "block";
    document.querySelector("#resultado").innerText = result.outcome;

  } catch (error) {
    document.querySelector("#resultado").innerText =
      "Erro ao processar a requisição.";
  }

})

async function pesquisarIndividuo(idIndividuo) {
  try {
    const container = document.getElementById("modal-conteudo");
    container.innerHTML = "<p>Carregando...</p>";

    const response = await fetch(`${API_URL}/individuos/${idIndividuo}`);
    
    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }

    const data = await response.json();

    container.innerHTML = `
      <h2>Detalhes do Indivíduo</h2>

      <table border="1" style="width:100%; border-collapse: collapse;">
        <tbody>
          <tr><th>ID</th><td>${data.id}</td></tr>
          <tr><th>Nome</th><td>${data.name}</td></tr>
          <tr><th>CPF</th><td>${data.cpf}</td></tr>
          <tr><th>Idade</th><td>${data.age}</td></tr>
          <tr><th>Gênero</th><td>${data.gender}</td></tr>
          <tr><th>Status</th><td>${data.student_working_status}</td></tr>

          <tr><th>Preferência de Conteúdo</th><td>${data.content_type_preference}</td></tr>
          <tr><th>Tempo de Tela (h)</th><td>${data.screen_time_hours}</td></tr>
          <tr><th>Horas de Sono</th><td>${data.daily_sleep_hours}</td></tr>
          <tr><th>Qualidade do Sono</th><td>${data.sleep_quality_score}</td></tr>

          <tr><th>Motivação</th><td>${data.motivation_level}</td></tr>
          <tr><th>Fadiga Emocional</th><td>${data.emotional_fatigue_score}</td></tr>

          <tr>
            <th>Risco de Burnout</th>
            <td><strong>${data.outcome}</strong></td>
          </tr>
        </tbody>
      </table>
    `;

    document.getElementById("modal-individuo").style.display = "flex";

  } catch (error) {
    console.error("Erro ao consumir API:", error);
  }
}

fecharModal.onclick = () => {
  modal.style.display = "none";
};

// Fecha ao clicar fora
window.onclick = (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
};

function resetForm() {
  form.reset();
  sectionResultado.style.display = "none";
  formSection.style.display = "none";
  sectionDescription.style.display = "block";
}

btnVoltarInicio.addEventListener("click", () => {
  resetForm();
});

btnFormVoltar.addEventListener("click", () => {
  resetForm();
});

btnInicicioResultados.addEventListener("click", () => {
  sectionDescription.style.display = "block";
  sectionResultados.style.display = "none";
});
