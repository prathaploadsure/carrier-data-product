import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './reducers'; // This path should match your file structure

const store = configureStore({
  reducer: rootReducer,
});

export default store;
