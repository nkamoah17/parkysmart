import React, { Component } from 'react';
import axios from 'axios';

class ApiKey extends Component {
  constructor(props) {
    super(props);
    this.state = {
      apiKey: '',
    };
  }

  componentDidMount() {
    this.getApiKey();
  }

  getApiKey = async () => {
    try {
      const response = await axios.get('/api-key');
      if (response.status === 200) {
        this.setState({ apiKey: response.data.key });
        this.props.onKeyChange(response.data.key);
      }
    } catch (error) {
      console.error('Error fetching API key:', error);
    }
  }

  render() {
    return (
      <div className="ApiKey">
        <h2>Your API Key:</h2>
        <p>{this.state.apiKey}</p>
      </div>
    );
  }
}

export default ApiKey;
