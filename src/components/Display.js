import React, { Component } from 'react';
import axios from 'axios';

class Display extends Component {
  constructor(props) {
    super(props);
    this.state = {
      occupancyData: null,
      isLoading: false,
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.imageId !== prevProps.imageId) {
      this.fetchOccupancyData();
    }
  }

  fetchOccupancyData = () => {
    this.setState({ isLoading: true });

    axios.get(`/occupancy/${this.props.imageId}`, {
      headers: {
        'api_key': this.props.apiKey
      }
    })
      .then((response) => {
        this.setState({ occupancyData: response.data, isLoading: false });
        this.props.onOccupancyData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching occupancy data: ", error);
        this.setState({ isLoading: false });
      });
  }

  render() {
    const { occupancyData, isLoading } = this.state;

    if (isLoading) {
      return <div>Loading...</div>;
    }

    if (!occupancyData) {
      return <div>No data available</div>;
    }

    return (
      <div>
        <h2>Occupancy Data</h2>
        <p>Total Spots: {occupancyData.totalSpots}</p>
        <p>Occupied Spots: {occupancyData.occupiedSpots}</p>
        <p>Free Spots: {occupancyData.freeSpots}</p>
      </div>
    );
  }
}

export default Display;
