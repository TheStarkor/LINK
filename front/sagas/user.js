import { all, delay, fork, put, takeEvery, call } from 'redux-saga/effects';
import axios from 'axios';
import { SIGN_UP_SUCCESS, SIGN_UP_FAILURE, SIGN_UP_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE, LOG_IN_REQUEST, LOG_OUT_FAILURE, LOG_OUT_REQUEST } from '../reducers/user';

function signUpAPI() {
  // ToDo
}

function* signUP() {
  try {
    yield delay(2000);
    yield put({
      type: SIGN_UP_SUCCESS,
    });
  } catch (e) {
    console.error(e);
    yield put({
      type: SIGN_UP_FAILURE,
      error: e,
    });
  }
}

function* watchSignUp() {
  yield takeEvery(SIGN_UP_REQUEST, signUP);
}

function loginAPI() {
  return axios.get("http://127.0.0.1:8000/api/")
}

function* login() {
  try {
    const result = yield call(loginAPI);
    yield put({
      type: LOG_IN_SUCCESS,
      data: result.data
    });
  } catch (e) {
    console.error(e);
    yield put({
      type: LOG_IN_FAILURE,
    });
  }
}

function* watchLogin() {
  yield takeEvery(LOG_IN_REQUEST, login);
}

function logoutAPI() {
  // ToDo
}

function* logout() {
  try {
    yield delay(2000);
    yield put ({
      type: LOG_OUT_SUCCESS
    });
  } catch (e) {
    console.error(e);
    yield put({
      type: LOG_OUT_FAILURE,
      error: e
    })
  }
}

function* watchLogout() {
  yield takeEvery(LOG_OUT_REQUEST, logout)
}

export default function* userSaga() {
  yield all([
    fork(watchSignUp),
    fork(watchLogin),
    fork(watchLogout),
  ]);
}