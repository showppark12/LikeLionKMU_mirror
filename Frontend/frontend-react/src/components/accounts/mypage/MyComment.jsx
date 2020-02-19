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

export default class MyComment extends Component {
  state = {
    studycomments: [],
    noticecomments: [],
    qnacomments: [],
    recruitcomments: [],
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
        var mystudy = myPosts.data.studycomments;
        var mynotice = myPosts.data.noticecomments;
        var myqna = myPosts.data.qnacomments;
        var myrecruit = myPosts.data.recruitcomments;
        
        this.setState({studycomments:mystudy});
        this.setState({noticecomments:mynotice});
        this.setState({qnacomments:myqna});
        this.setState({recruitcomments:myrecruit});

      })
      .catch(err => console.log(err));
  }

  render() {
    // const { id, title, body, purpose } = this.props;

    return (
      <Paper elevation={10} className="MyComment">
        <>
          <h1>My Comments</h1>
          <br />
          {this.state.noticecomments.map(mycomment => (
            <div>
              <h4>Notice board</h4>

              <Link
                to={`/notice/detail/${mycomment.id}`}
                className={"main-postTitle"}
              >
                -{mycomment.body}
              </Link>
            </div>
          ))}
          <br />
          {this.state.qnacomments.map(mycomment => (
            <div>
              <h4>QnA board</h4>
              <Link
                to={`/qna/detail/${mycomment.id}`}
                className={"main-postTitle"}
              >
                -{mycomment.body}
              </Link>
            </div>
          ))}
          <br />
          {this.state.studycomments.map(mycomment => (
            <div>
              <h4>study board</h4>
              <Link
                to={`/study/detail/${mycomment.id}`}
                className={"main-postTitle"}
              >
                -{mycomment.body}
              </Link>
            </div>
          ))}
          <br />
          {this.state.recruitcomments.map(mycomment => (
            <div>
              <h4>recruit board</h4>
              <Link
                to={`/recruit/detail/${mycomment.id}`}
                className={"main-postTitle"}
              >
                -{mycomment.body}
              </Link>
            </div>
          ))}
        </>
      </Paper>
    );
  }
}
