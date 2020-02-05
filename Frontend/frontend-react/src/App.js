import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import Main from "./components/main/Main";

import Login from "./components/accounts/LoginContainer";
import Mypage from "./components/accounts/Mypage";
import Store from "./Store/store";

import NoticeList from "./components/board/NoticeList";
import NoticeDetail from "./components/board/NoticeDetail";
import NoticeNew from "./components/board/NoticeNew";
import NoticeUpdate from "./components/board/NoticeUpdate";

import QnANew from "./components/board/QnANew";
import QnAList from "./components/board/QnAList";
import QnADetail from "./components/board/QnADetail";
import QnAUpdate from "./components/board/QnAUpdate";

import StudyNew from "./components/board/StudyNew";
import StudyList from "./components/board/StudyList";
import StudyDetail from "./components/board/StudyDetail";
import StudyUpdate from "./components/board/StudyUpdate";

import RecruitNew from "./components/board/RecruitNew";
import RecruitList from "./components/board/RecruitList";
import RecruitDetail from "./components/board/RecruitDetail";
import RecruitUpdate from "./components/board/RecruitUpdate";



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      logged: false,
      onLogin: this.onLogin,
      onLogout: this.onLogout
    };
  }

  onLogin = () => {
    this.setState({
      logged: true
    });
    console.log("login 되었습니다.");
  };

  onLogout = () => {
    this.setState({
      logged: false
    });
    console.log("logout 되었습니다.");
    // const token = window.sessionStorage.getItem('token');
    window.sessionStorage.clear();
  };

  componentDidMount() {
    // const name = window.sessionStorage.getItem("name");
    const id = window.sessionStorage.getItem("id");

    if (id) {
      this.onLogin();
    } else {
      this.onLogout();
    }
  }

  render() {
    const { logged, onLogout } = this.state;

    return (
      <Store.Provider value={this.state}>
        <Router>
          <Header logged={logged} onLogout={onLogout} />
          <Route exact path="/" component={Main} />

          <Route exact path="/notice" component={NoticeList} />
          <Route exact path="/notice/new" component={NoticeNew} />
          <Route path="/notice/detail/:id" component={NoticeDetail} id="number" />
          <Route path="/notice/update/:id" component={NoticeUpdate} id="number" />

          <Route exact path="/QnA" component={QnAList} />
          <Route exact path="/QnA/new" component={QnANew} />
          <Route path="/QnA/detail/:id" component={QnADetail} id="number" />
          <Route path="/QnA/update/:id" component={QnAUpdate} id="number" />

          <Route exact path="/study" component={StudyList} />
          <Route exact path="/study/new" component={StudyNew} />
          <Route path="/study/detail/:id" component={StudyDetail} id="number" />
          <Route path="/study/update/:id" component={StudyUpdate} id="number" />

          <Route exact path="/recruit" component={RecruitList} />
          <Route exact path="/recruit/new" component={RecruitNew} />
          <Route path="/recruit/detail/:id" component={RecruitDetail} id="number" />
          <Route path="/recruit/update/:id" component={RecruitUpdate} id="number" />



          <Route path="/login" component={Login} />
          <Route path="/mypage/:id" component={Mypage} id="number" />
          <Footer />
        </Router>
      </Store.Provider>
    );
  }
}

export default App;
