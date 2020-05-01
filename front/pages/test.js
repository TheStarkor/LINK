import React from 'react';
import axios from 'axios';
import { Button } from 'antd';

const Test = () => {
  const dummy = {
    title: "title test",
    author: "bsh",
    pw: "hello1234",
    content: "Test Test Test"
  }

  const dummyUser1 = {
    email: "ab@a.com",
    portal_id: "abcd",
    name: "testtt",
    dept_major: "cs",
    username: "hoho",
    reputation: "repurepu",
    password: "1234abc"
  }
  const dummyUser2 = {
    email: "adwdaw@dw.com",
    portal_id: "dawf",
    name: "ssdwfasdw",
    dept_major: "css",
    username: "gglgg",
    reputation: "repurdadawu",
    password: "1sdwdwdc"
  }
  const dummyfind = {
    portal_id: "abcd",
    password: "1234abc"
  }

  const getTest = async () => {
    const response = await axios.get("http://127.0.0.1:8000/api/")
    console.log('===> GET test : ', response.data)
  }

  const postTest = async () => {
    const response = await axios.post("http://127.0.0.1:8000/api/", dummy)
    console.log('===> POST test: ', response.data)
  }

  const registerTest1 = async () => {
    const response = await axios.post("http://127.0.0.1:8000/accounts/api/register", 
                                      dummyUser1)
    console.log('===> Register test: ', response.data)
  }

  const registerTest2 = async () => {
    const response = await axios.post("http://127.0.0.1:8000/accounts/api/register", 
                                      dummyUser2)
    console.log('===> Register test: ', response.data)
  }

  const loginTest = async () => {
    const response = await axios.post("http://127.0.0.1:8000/accounts/api/login",
                                      dummyUser1)
    console.log('===> Login test: ', response.data)                            
  }

  const findaccountTest = async () => {
    const response = await axios.post("http://127.0.0.1:8000/accounts/api/findaccount",
                                      dummyfind)
    console.log('===> Find Account test: ', response.data)      
  }

  return (
    <>
      <div>
        <Button onClick={getTest}>GET test</Button>
        <Button onClick={postTest}>POST test</Button>
        <Button onClick={registerTest1}>Register test 1</Button>
        <Button onClick={registerTest2}>Register test 2</Button>
      </div>
      <div>
        <Button onClick={loginTest}>Login test</Button>
        <Button onClick={findaccountTest}>Find Account test</Button>
      </div>
    </>
  )
}

export default Test