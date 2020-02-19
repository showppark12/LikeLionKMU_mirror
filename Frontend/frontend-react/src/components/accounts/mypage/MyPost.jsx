import React, { Component } from "react";
import { Link } from "react-router-dom";
import Paper from "@material-ui/core/Paper";
import api from "../../../api/BoardAPI";
// import Card from '@material-ui/core/Card';
// import CardActions from '@material-ui/core/CardActions';
// import CardContent from '@material-ui/core/CardContent';
// import Typography from '@material-ui/core/Typography';
// import PropTypes from 'prop-types';
// import { makeStyles } from '@material-ui/core/styles';
// import ListItem from '@material-ui/core/ListItem';
// import ListItemText from '@material-ui/core/ListItemText';
// import {FixedSizeList} from 'react-window';

export default class MyPost extends Component {
  state = {
    studyboard: [],
    noticeboard: [],
    qnaboard: [],
    recruitboard: [],
  };
  componentDidMount() {
    const id = this.props.id;
    this.getMyPost(id);
  }

  async getMyPost(id) {
    await api
      .getMyPost(id)
      .then(myPosts => {
        console.log(myPosts);
        var mystudy = myPosts.data.studyboard;
        var mynotice = myPosts.data.noticeboard;
        var myqna = myPosts.data.qnaboard;
        var myrecruit = myPosts.data.recruitboard;
        
        this.setState({studyboard:mystudy});
        this.setState({noticeboard:mynotice});
        this.setState({qnaboard:myqna});
        this.setState({recruitboard:myrecruit});

      })
      .catch(err => console.log(err));
  }

  render() {
    // const { id, title, body, purpose } = this.props;

    return (
      <Paper elevation={10} className="MyPost">
        <>
          <h1>My Post</h1>
          <br />
          {this.state.noticeboard.map(mypost => (
            <div>
              <h4>Notice board</h4>

              <Link
                to={`/notice/detail/${mypost.id}`}
                className={"main-postTitle"}
              >
                -{mypost.title}
              </Link>
            </div>
          ))}
          <br />
          {this.state.qnaboard.map(mypost => (
            <div>
              <h4>QnA board</h4>
              <Link
                to={`/qna/detail/${mypost.id}`}
                className={"main-postTitle"}
              >
                -{mypost.title}
              </Link>
            </div>
          ))}
          <br />
          {this.state.studyboard.map(mypost => (
            <div>
              <h4>study board</h4>
              <Link
                to={`/study/detail/${mypost.id}`}
                className={"main-postTitle"}
              >
                -{mypost.title}
              </Link>
            </div>
          ))}
          <br />
          {this.state.recruitboard.map(mypost => (
            <div>
              <h4>recruit board</h4>
              <Link
                to={`/recruit/detail/${mypost.id}`}
                className={"main-postTitle"}
              >
                -{mypost.title}
              </Link>
            </div>
          ))}
        </>
      </Paper>
    );
  }
}
