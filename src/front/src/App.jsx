import { useState } from "react";
import { Button, Card } from "@mui/material";
import { BarChart } from "@mui/x-charts";
import { CloudUpload } from "@mui/icons-material";

function App() {
  const [response, setResponse] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [isLoading, setIsLoading] = useState(null);

  const labelsTranslated = {
    no_finding: "Sem achados patológicos",
    enlarged_cardiomediastinum: "Cardiomediastino aumentado",
    cardiomegaly: "Cardiomegalia",
    lung_opacity: "Opacidade pulmonar",
    lung_lesion: "Lesão pulmonar",
    edema: "Edema pulmonar",
    consolidation: "Consolidação",
    pneumonia: "Pneumonia",
    atelectasis: "Atelectasia",
    pneumothorax: "Pneumotórax",
    pleural_effusion: "Derrame pleural",
    pleural_other: "Outras alterações pleurais",
    fracture: "Fratura",
    support_devices: "Dispositivos de suporte",
  };

  const requestPredict = async () => {
    if (!selectedFile) return alert("Selecione um arquivo de Raio X.");

    setIsLoading(true);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const resp = await fetch("http://localhost/predict", {
        method: "POST",
        body: formData,
      });

      const data = await resp.json();
      console.log(data);
      if (resp.ok) {
        const dataFormatted = Object.entries(data).map(([key, value]) => ({
          name: labelsTranslated[key] ?? key,
          value: value,
        }));

        setResponse(dataFormatted);
        setIsLoading(false);
      } else {
        setIsLoading(false);
        alert("Houve um erro interno na API de predição do Raio X.");
      }
    } catch (error) {
      setIsLoading(false);
      alert("Houve um erro ao subir o arquivo.");
      console.log("Erro ao subir o arquivo", error);
    }
  };

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  return (
    <>
      {response != null && (
        <Card style={{ width: "800px", maxWidth: "90vw", padding: 20 }}>
          <BarChart
            dataset={response}
            yAxis={[
              {
                scaleType: "band",
                dataKey: "name",
                labelStyle: { fontSize: 14 },
                tickLabelStyle: { fontSize: 14, whiteSpace: "normal" },
                width: 300,
              },
            ]}
            series={[
              {
                dataKey: "value",
                label: "Probabilidade",
                valueFormatter: (v) => `${v}%`,
              },
            ]}
            xAxis={[
              {
                label: "Probabilidades (%)",
                min: 0,
                max: 100,
              },
            ]}
            layout="horizontal"
            height={400}
          />

          <Button
            variant="contained"
            component="label"
            loading={isLoading}
            disabled={isLoading}
            color="primary"
            startIcon={<CloudUpload />}
            fullWidth
          >
            Escolher Raio X
            <input
              type="file"
              hidden
              accept="image/png, image/jpeg"
              onChange={handleFileChange}
              multiple={false}
            />
          </Button>

          <Button
            onClick={requestPredict}
            fullWidth
            variant="outlined"
            loading={isLoading}
            disabled={isLoading}
            style={{ marginTop: 20 }}
          >
            Enviar Raio X
          </Button>
        </Card>
      )}
      {response == null && (
        <Card style={{ width: "800px", maxWidth: "90vw", padding: 20 }}>
          <Button
            variant="contained"
            component="label"
            loading={isLoading}
            disabled={isLoading}
            color="primary"
            startIcon={<CloudUpload />}
            fullWidth
          >
            Escolher Raio X
            <input
              type="file"
              hidden
              accept="image/png, image/jpeg"
              onChange={handleFileChange}
              multiple={false}
            />
          </Button>
          {selectedFile != null && <p>{selectedFile.name} carregado.</p>}

          <Button
            onClick={requestPredict}
            fullWidth
            loading={isLoading}
            disabled={isLoading}
            variant="outlined"
            style={{ marginTop: 20 }}
          >
            Enviar Raio X
          </Button>
        </Card>
      )}
    </>
  );
}

export default App;
