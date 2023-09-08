import React, { Component } from 'react';
import axios from 'axios';

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: null,
    };
  }

  handleFileChange = (event) => {
    this.setState({ selectedFile: event.target.files[0] });
  }

  handleUpload = () => {
    const data = new FormData();
    data.append('file', this.state.selectedFile);
    data.append('api_key', this.props.apiKey);

    axios.post('/upload', data)
      .then((response) => {
        this.props.onUpload(response.data.imageId);
      })
      .catch((error) => {
        console.error("Error uploading file: ", error);
      });
  }

  render() {
    return (
      <div>
        <input type="file" onChange={this.handleFileChange} />
        <button onClick={this.handleUpload}>Upload</button>
      </div>
    );
  }
}

export default Upload;
