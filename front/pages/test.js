import React from 'react';
import axios from 'axios';
import { Button } from 'antd';

const Test = () => {
  const dummy = {
    id: 123,
    test: 'helloo'
  }

  const getTest = async () => {
    const response = await axios.get("http://127.0.0.1:8000/api/")
    console.log('===> GET test : ', response.data)
  }

  const postTest = async () => {
    const response = await axios.post("http://127.0.0.1:8000/api/", dummy)
    console.log('===> POST test: ', response.data)
  }

  return (
    <>
      <div>
        <Button onClick={getTest}>GET test</Button>
        <Button onClick={postTest}>POST test</Button>
      </div>
    </>
  )
}

export default Test