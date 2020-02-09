import React from "react";
import api from "../../api/api_board";
import RecentPost from "./RecentPost";

import logo from "./logo.png";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";

import Carousel from "react-bootstrap/Carousel";

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recentNotices: [],
      recentQnA: []
    };
  }
  componentDidMount() {
    this.getRecentPosts("notice");
    this.getRecentPosts("QnA");
  }

  async getRecentPosts(target) {
    await api
      .getAllPosts(target)
      .then(recentPosts => {
        console.log(recentPosts);
        var posts = recentPosts.data.results;
        var slicePosts = posts.slice(0, 4);
        switch (target) {
          case "notice":
            this.setState({ recentNotices: slicePosts });
            break;
          case "QnA":
            this.setState({ recentQnA: slicePosts });
            break;
          default:
            break;
        }
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        <Container maxWidth="lg" className="main-container">
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <Carousel>
                <Carousel.Item>
                  <img className="d-block w-100" src={logo} alt="logo" />
                </Carousel.Item>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src={logo}
                    alt="Second slide"
                  />
                </Carousel.Item>
                <Carousel.Item>
                  <img className="d-block w-100" src={logo} alt="Third slide" />
                  <Carousel.Caption>
                    <h3>Third slide label</h3>
                  </Carousel.Caption>
                </Carousel.Item>
              </Carousel>
            </Grid>
          </Grid>
          <hr />
          <div>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <h4 className={"main-recentTitle"}>최근 공지사항</h4>
                <Paper>
                  {this.state.recentNotices.map(post => (
                    <RecentPost
                      key={post.id}
                      id={post.id}
                      title={post.title}
                      body={post.body}
                    />
                  ))}
                </Paper>
              </Grid>
              <Grid item xs={12} sm={6}>
                <h4 className={"main-recentTitle"}>최근 QnA</h4>
                <Paper>
                  {this.state.recentQnA.map(post => (
                    <RecentPost
                      key={post.id}
                      id={post.id}
                      title={post.title}
                      body={post.body}
                    />
                  ))}
                </Paper>
              </Grid>
            </Grid>
          </div>
          <hr />
          <div>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={12}>
                일정 캘린더
              </Grid>
            </Grid>
          </div>
          <hr />
          <div>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={12}>
                What We Made!
              </Grid>
            </Grid>
          </div>
        </Container>
      </div>
    );
  }
}

export default Main;
