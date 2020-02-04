import React, { Component } from "react";
// import api from "../../api/api_auth";
// import { Link } from "react-router-dom";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";

class Mypage extends Component {
  state = {
    id: "",
    username: "",
    password: "",
    token: ""
  };

  componentDidMount() {
    console.log("New ComponentDidMount");
    const _id = window.sessionStorage.getItem("id");
    const _user = window.sessionStorage.getItem("username");

    this.setState({
      id: _id,
      username: _user
    });
    // this.getUser(_id);
  }

  // async getUser(userId) {
  //   await api
  //     .getUser(userId)
  //     .then(res => {
  //       const userData = res.data;
  //       console.log(userData);
  //       this.setState({
  //         id: userData.id,
  //         username: userData.username
  //       });
  //     })
  //     .catch(err => console.log(err));
  // }

  render() {
    return (
      <Container maxWidth="lg" className="PostingSection">
        <Paper className="PostingPaper">
          <h2>My page</h2>
          id {this.state.id} <br />
          Username {this.state.username}
          <br />
        </Paper>
      </Container>
    );
  }
}

export default Mypage;
