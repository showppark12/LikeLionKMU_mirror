import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import Main from "./components/main/Main";

import Login from "./components/accounts/login";
import Mypage from "./components/accounts/mypage/Mypage";
import Store from "./store/store";

import { authlogout, tokenConfig } from "./api/AuthAPI";

import BoardRouter from "./routes/BoardRouter";
import StudyRouter from "./routes/StudyRouter";
// import AdmissionRouter from "./components/admission/AdmissionRouter";

import MentoringContainer from "./components/mentoring/MentoringContainer";

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
  };

  onLogout = async () => {
    if (this.state.logged) {
      // console.log(tokenConfig());
      await authlogout(tokenConfig())
        .then(() => {
          this.setState({
            logged: false
          });
          window.sessionStorage.clear();
          console.log("logout 되었습니다.");
        })
        .catch(err => {
          console.log(err);
        });
    }
  };

  componentDidMount() {
    const token = window.sessionStorage.getItem("token");
    if (token) {
      this.onLogin();
    } else {
      this.onLogout();
    }
  }

  render() {
    return (
      <Store.Provider value={this.state}>
        <Router>
          <Header />
          <Route exact path="/" component={Main} />

          <Route path="/notice" component={BoardRouter} />
          <Route path="/QnA" component={BoardRouter} />
          <Route path="/study" component={StudyRouter} />
          <Route path="/recruit" component={BoardRouter} />

          {/* <Route path="/admission" component={AdmissionRouter} /> */}
          <Route path="/mentoring" component={MentoringContainer} />

          <Route path="/login" component={Login} />
          <Route path="/mypage/:id" component={Mypage} id="number" />
          <Footer />
        </Router>
      </Store.Provider>
    );
  }
}

export default App;
