import { all, delay, fork, put, takeEvery } from 'redux-saga/effects';
import { SIGN_UP_SUCCESS, SIGN_UP_FAILURE, SIGN_UP_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE, LOG_IN_REQUEST } from '../reducers/user';

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
  // ToDo
}

function* login() {
  try {
    yield delay(2000);
    yield put({
      type: LOG_IN_SUCCESS,
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

export default function* userSaga() {
  yield all([
    fork(watchSignUp),
    fork(watchLogin),
  ]);
}