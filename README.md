# LINK
Link IN Knowledge

### Documentation
Documentation for the DB, API, and Web is available on the [Gitbook](https://sk-and-mc.gitbook.io/link/)

## Getting Started

### Start Front Server  
- Environment: [Node.js 10.15](https://nodejs.org/en/) (npm)
```
$ cd front
$ npm install
$ npm run dev
```

### Start Django Back Server  
- Environment: [Python 3.7](https://www.python.org/) (virtualenv)
```
$ cd back_django
$ virtualenv <env name>
$ source <env name>/Scripts/activate
$ pip install -r requirement.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Built with
- [React.js](https://reactjs.org/)
  - [Next.js](https://nextjs.org/)
  - [Redux](https://redux.js.org/)
  - [Redux-Saga](https://redux-saga.js.org/)
  - [Sass, SCSS](https://sass-lang.com/)
- [Django](https://www.djangoproject.com/)
  - [Django REST framework](https://www.django-rest-framework.org/)
  - [Black](https://github.com/psf/black)

## Directory

```
LINK
├── back
├── back_django     // django api test server
├── front
│   ├── components  // React Components
│   ├── pages       // The root of a Next.js application
│   ├── reducers
│   └── sagas
├── LICENSE
└── README.md
```

## Git Commit Message Style

We follows https://udacity.github.io/git-styleguide/

```
feat: a new feature
fix: a bug fix
docs: changes to documentation
style: formatting, missing semi colons, etc; no code change
refactor: refactoring production code
test: adding tests, refactoring test; no production code change
chore: updating build tasks, package manager configs
```