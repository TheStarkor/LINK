import React from 'react';
import Link from 'next/link';
import PropTypes from 'prop-types';
import { Menu, Input, Row, Col } from 'antd';
import { useSelector } from 'react-redux';

import LoginForm from './LoginForm';
import UserProfile from './UserProfile';

const AppLayout = ({ children }) => {
  const { me } = useSelector(state => state.user);

  return (
    <div>
      <Menu mode="horizontal">
        <Menu.Item key="home"><Link href="/"><a>LINK</a></Link></Menu.Item>
        <Menu.Item key="mail">
          <Input.Search 
            enterButton
            style={{ verticalAlign: 'middle' }}/>
        </Menu.Item>
        <Menu.Item key="profile"><Link href="/profile"><a>프로필</a></Link></Menu.Item>
      </Menu>
      <Row gutter={8}>
        <Col x={24} md={6}>
          {me
            ? <UserProfile />
            : <LoginForm />}
        </Col>
        <Col xs={24} md={18}>
          {children}
        </Col>
      </Row>
    </div>
  )
};

AppLayout.propTypes = {
  children: PropTypes.element
};

export default AppLayout