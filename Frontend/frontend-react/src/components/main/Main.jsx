import React from "react";
import api from "../../api/BoardAPI";
// import RecentPost from "./RecentPost";
import RecentPost from "../board/container/PostView";

import logo from "./logo.png";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
//  import Paper from "@material-ui/core/Paper";

import Carousel from "react-bootstrap/Carousel";
import { ClubCalendar } from "../calendar/ClubCalendar";

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recentNotices: [],
      recentQnA: [],
      recentCareer: [],
    };
  }
  componentDidMount() {
    this.getRecentPosts("notice");
    this.getRecentPosts("qna");
    this.getRecentPosts("career");
  }

  async getRecentPosts(target) {
    await api
      .getAllPosts(target)
      .then(recentPosts => {
        console.log(recentPosts);
        var posts = recentPosts.data;
        var slicePosts = posts.slice(0, 4);
        switch (target) {
          case "notice":
            this.setState({ recentNotices: slicePosts });
            break;
          case "qna":
            this.setState({ recentQnA: slicePosts });
            break;
          case "career":
            this.setState({ recentCareer: slicePosts });
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
                  {/* <Carousel.Caption>
                    <h3>Third slide label</h3>
                  </Carousel.Caption> */}
                </Carousel.Item>
              </Carousel>
            </Grid>
          </Grid>
          <hr />
          <div>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <h4 className={"main-recentTitle"}>최근 공지사항</h4>
                {this.state.recentNotices.map(notice_post => (
                  <RecentPost
                    key={notice_post.id}
                    postInfo={notice_post}
                    board_name="notice"
                  />
                ))}
              </Grid>
              <Grid item xs={12} sm={6}>
                <h4 className={"main-recentTitle"}>최근 QnA</h4>
                {this.state.recentQnA.map(qna_post => (
                  <RecentPost
                    key={qna_post.id}
                    postInfo={qna_post}
                    board_name="QnA"
                  />
                ))}
              </Grid>
            </Grid>
          </div>
          <hr />
          <div>
            <ClubCalendar />
          </div>
          <hr />
          <div>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={12}>
                <h4 className={"main-recentTitle"}>What We Made!</h4>
                  {this.state.recentCareer.map(career_post => (
                    <RecentPost
                      key={career_post.id}
                      postInfo={career_post}
                      board_name="career"
                    />
                  ))}
              </Grid>
            </Grid>
          </div>
        </Container>
      </div>
    );
  }
}

export default Main;
