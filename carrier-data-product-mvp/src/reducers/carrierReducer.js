const initialState = {
    carrierOverview: null, // or an empty object {} if you prefer
    // other state properties...
  };
  
  const carrierReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'FETCH_CARRIER_OVERVIEW_SUCCESS':
        return {
          ...state,
          carrierOverview: action.payload,
        };
      // other cases...
      default:
        return state;
    }
  };
  
  export default carrierReducer;
  