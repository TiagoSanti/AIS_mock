import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { LinearProgress } from '@mui/material';
import '../styles/global.css';
import '../styles/csv-upload.css';
import send from '../assets/send.svg';

const CsvUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      setFile(null);
      setUploadProgress(0);
      toast.info('Nenhum arquivo selecionado.');
      return;
    }

    const maxSize = 200 * 1024 * 1024; // 200MB
    if (selectedFile.size > maxSize) {
      toast.error('O arquivo selecionado é maior que 200MB. Por favor, escolha um arquivo menor.');
      setFile(null);
      setUploadProgress(0);
      return;
    }
    setUploading(false);
    setFile(selectedFile);
  };

  const handleUpload = async () => {
    if (!file) {
      toast.error('Por favor, escolha um arquivo.');
      return;
    }

    const fileId = uuidv4();
    const formData = new FormData();
    formData.append('file', file);

    try {
      setUploading(true);
      const response = await fetch(`http://localhost:8000/upload/${fileId}`, {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const result = await response.json();
        toast.success('Arquivo enviado com sucesso!');
        const fileNameWithoutExtension = file.name.split('.').slice(0, -1).join('.');
        onUploadSuccess(fileId, fileNameWithoutExtension);
      } else {
        throw new Error('Falha ao enviar arquivo.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      toast.error('Falha ao enviar arquivo.');
    } finally {
      setUploading(false);
      setUploadProgress(0);
    }
  };

  return (
    <div className="home_csv_upload">
      <div className="home_csv_upload_buttons">
        <label htmlFor="home_csv_upload_input" className="home_csv_choose_button">
          Escolher arquivo
        </label>
        <input
          id="home_csv_upload_input"
          className="home_csv_upload_hidden"
          type="file"
          accept=".csv"
          onChange={handleFileChange}
        />
        <button
          className={`home_csv_send_button ${uploading ? 'disabled' : ''}`}
          onClick={handleUpload}
          disabled={uploading}
        >
          Enviar arquivo
          <img src={send} alt="send" className="home_csv_send_button_image" />
        </button>
      </div>
      {file && (
        <div className="home_file_name_display">
          <span>{file.name}</span>
        </div>
      )}
      {uploadProgress > 0 && (
        <LinearProgress variant="determinate" value={uploadProgress} className='home_progress_bar'/>
      )}
      <div className="home_csv_info">
        <p className="home_csv_upload_limit">Limite: 200 Mb</p>
        <a href='https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/download?datasetVersionNumber=3'>Clique aqui para baixar o dataset e experimentar a aplicação.</a>
        <p className='home_csv_upload_warning'>Ao inserir o conjunto de dados, por gentileza, verifique se o label das classes estão na coluna "Class".</p>
      </div>
    </div>
  );
};

export default CsvUpload;
