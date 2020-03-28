import React from 'react';
import Head from 'next/head';
import PropTypes from 'prop-types';
import AppLayout from '../components/AppLayout';

const LINK = ({ Component }) => {
  return (
    <>
      <Head>
        <title>LINK</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/antd/4.0.1/antd.css"/>
      </Head>
      Hello
      <AppLayout>
        <Component />
      </AppLayout>
    </>
  )
};

LINK.propTypes = {
  Component: PropTypes.elementType
};

export default LINK;