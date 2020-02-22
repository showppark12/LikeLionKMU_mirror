import React, { Component } from "react";
import api from "../../../api/BoardAPI";
import { Link } from "react-router-dom";
// import moment from "moment";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";


class QnAUpdate extends Component {
  state = {
    title: "",
    body: "",
    subject: ""
  };

  componentDidMount() {
    console.log("Detail ComponentDidMount");
    //this._getQnA(this.props.match.params.id);
    this.getQnA();
  }

  async getQnA() {
    await api
      .getPost("qna", this.props.match.params.id)
      .then(res => {
        const data = res.data;

        this.setState({
          title: data.title,
          body: data.body,
          id: data.id,
          subject: data.subject
        });
      })
      .catch(err => console.log(err));
  }
  async updateQnA(id, data) {
    await api
      .updatePost("qna", id, data)
      .then(result => console.log("정상적으로 update됨.", result))
      .catch(err => console.log(err));
  }

  handlingChange = event => {
    this.setState({ [event.target.name]: event.target.value });
  };

  handlingSubmit = async event => {
    event.preventDefault(); //event의 디폴트 기능(새로고침 되는 것 등..) -> 막는다.
    this.updateQnA(this.props.match.params.id, {
      title: this.state.title,
      body: this.state.body,
      subject: this.state.subject
    });
    this.setState({ title: "", content: "", subject: "" });
    // this.getPosts()
    document.location.href = "/QnA";
  };

  render() {
    return (
      <Container maxWidth="lg" className="PostingSection">
        <Paper className="PostingPaper">
          <h2>Update QnA</h2>
          <form onSubmit={this.handlingSubmit} className="PostingForm">
            <input
              id="title"
              name="title"
              value={this.state.title}
              onChange={this.handlingChange}
              required="required"
              placeholder="Title"
            />
            <input
              id="body"
              name="body"
              value={this.state.body}
              onChange={this.handlingChange}
              required="required"
              placeholder="Content"
            />
            <input
              name="subject"
              value={this.state.subject}
              onChange={this.handlingChange}
              required="required"
              placeholder="Subject"
            />

            <button type="submit">제출</button>
          </form>

          <Link to="/QnA">Cancel</Link>
        </Paper>
      </Container>
    );
  }
}

export default QnAUpdate;