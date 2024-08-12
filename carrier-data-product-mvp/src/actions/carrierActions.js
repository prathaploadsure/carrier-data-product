// src/actions/carrierActions.js
import axios from 'axios'; // You can use 'fetch' instead if you prefer

export const FETCH_CARRIER_OVERVIEW_REQUEST = 'FETCH_CARRIER_OVERVIEW_REQUEST';
export const FETCH_CARRIER_OVERVIEW_SUCCESS = 'FETCH_CARRIER_OVERVIEW_SUCCESS';
export const FETCH_CARRIER_OVERVIEW_FAILURE = 'FETCH_CARRIER_OVERVIEW_FAILURE';

export const fetchCarrierOverviewRequest = () => ({
  type: FETCH_CARRIER_OVERVIEW_REQUEST
});

export const fetchCarrierOverviewSuccess = (carrierOverview) => ({
  type: FETCH_CARRIER_OVERVIEW_SUCCESS,
  payload: carrierOverview
});

export const fetchCarrierOverviewFailure = (error) => ({
  type: FETCH_CARRIER_OVERVIEW_FAILURE,
  payload: error
});

export const fetchCarrierOverview = () => {
  return (dispatch) => {
    dispatch(fetchCarrierOverviewRequest());
    return axios.get('/carrier/overview') // Adjust the URL if your API is on a different port or domain
      .then(response => {
        dispatch(fetchCarrierOverviewSuccess(response.data));
      })
      .catch(error => {
        dispatch(fetchCarrierOverviewFailure(error.message));
      });
  };
};
