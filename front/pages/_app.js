import React from 'react';
import Head from 'next/head';
import PropTypes from 'prop-types';
import withRedux from 'next-redux-wrapper';
import { applyMiddleware, compose, createStore } from 'redux';
import { Provider } from 'react-redux';
import AppLayout from '../components/AppLayout';
import reducer from '../reducers';

const LINK = ({ Component, store }) => {
  return (
    <>
      <Provider store={store}>
        <Head>
          <title>LINK</title>
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/antd/4.0.1/antd.css"/>
        </Head>
        <AppLayout>
          <Component />
        </AppLayout>
      </Provider>
    </>
  )
};

LINK.propTypes = {
  Component: PropTypes.elementType,
  store: PropTypes.object,
};

export default withRedux((initialState, options) => {
  const middlewares = [];
  const enhancer = compose(
    applyMiddleware(...middlewares),
    !options.isServer 
    && typeof window.__REDUX_DEVTOOLS_EXTENSION__ !== 'undefined' 
      ? window.__REDUX_DEVTOOLS_EXTENSION__() 
      : (f) => f,
  );
  const store = createStore(reducer, initialState, enhancer);
  return store;
})(LINK);
