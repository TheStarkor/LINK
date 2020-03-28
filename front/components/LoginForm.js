import React, { useState, useCallback } from 'react';
import Link from 'next/link';
import { Input, Button, Form } from 'antd';

export const useInput = (initValue = null) => {
  const [value, setter] = useState(initValue);
  const handler = useCallback((e) => {
    setter(e.target.value);
  }, []);
  return [value, handler];
};

const LoginForm = () => {
  const [id, onChangeId] = useInput('');
  const [password, onChangePassword] = useInput('');

  const onFinish = useCallback(() => {
    // ToDo
    console.log(`id: ${id}, password: ${password}`);
  }, [id, password]);
  
  return (
    <Form onFinish={onFinish} style={{ padding: '10px'}}>
      <div>
        <label htmlFor="user-id">아이디</label>
        <br />
        <Input
          name="user-id"
          value={id}
          onChange={onChangeId}
          required
        />
      </div>
      <div>
        <label htmlFor="user-password">비밀번호</label>
        <br />
        <Input 
          name="user-password"
          type="password"
          required
          value={password}
          onChange={onChangePassword}
        />
      </div>
      <div style={{ marginTop: '10px'}}>
        <Button type="primary" htmlType="submit">로그인</Button>
        <Link href="/signup"><a><Button>회원가입</Button></a></Link>
      </div>
    </Form>
  )
};

export default LoginForm;