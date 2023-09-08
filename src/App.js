import React, { Component } from 'react';
import Upload from './components/Upload';
import Display from './components/Display';
import ApiKey from './components/ApiKey';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      apiKey: '',
      occupancyData: {},
      currentImageId: null,
    };
  }

  handleApiKey = (key) => {
    this.setState({ apiKey: key });
  }

  handleUpload = (imageId) => {
    this.setState({ currentImageId: imageId });
  }

  handleOccupancyData = (data) => {
    this.setState({ occupancyData: data });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">AI-Powered Parking Lot Occupancy</h1>
        </header>
        <ApiKey onKeyChange={this.handleApiKey} />
        <Upload apiKey={this.state.apiKey} onUpload={this.handleUpload} />
        <Display apiKey={this.state.apiKey} imageId={this.state.currentImageId} onOccupancyData={this.handleOccupancyData} />
      </div>
    );
  }
}

export default App;
