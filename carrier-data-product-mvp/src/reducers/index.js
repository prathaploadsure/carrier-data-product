import { combineReducers } from 'redux';
import carrierReducer from './carrierReducer';

const rootReducer = combineReducers({
  carrier: carrierReducer
  // Add other reducers here
});

export default rootReducer;
