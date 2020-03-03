import React from "react";

import api from "../../api/SessionAPI";
// import { Link } from "react-router-dom";
// import { getAllUser } from "../../api/AuthAPI";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import ScoreNew from "./ScoreNew";
import ScoreView from "./ScoreView";

class GradingView extends React.Component {
  state = { isLoading: true };

  componentDidMount() {}

  handlingChange = event => {
    this.setState({ [event.target.name]: event.target.value });
  };

  render() {
    const {
      memberId,
      member,
      submissionInfo,
      assignmentId,
      getSubmission
    } = this.props;
    if (memberId === "") {
      return <>...</>;
    } else {
      return (
        <>
          {submissionInfo.length === 0 ? (
            <>
              <Card variant="outlined">
                <CardContent>
                  <Typography color="textSecondary" gutterBottom>
                    ID :: {memberId}
                  </Typography>
                  <Typography variant="h5" component="h2">
                    {member.first_name}({member.username})
                  </Typography>
                  <Typography color="textSecondary">제출기록 :: --</Typography>
                  <Typography variant="body2" component="p">
                    제출물이 없습니다.
                  </Typography>
                </CardContent>
                <CardActions></CardActions>
              </Card>
            </>
          ) : (
            <>
              <Card variant="outlined">
                <CardContent>
                  <Typography color="textSecondary" gutterBottom>
                    ID :: {memberId}
                  </Typography>
                  <Typography variant="h5" component="h2">
                    {member.first_name}({member.username})
                  </Typography>
                  <Typography color="textSecondary">
                    제출기록 :: {submissionInfo[0].update_date}
                  </Typography>
                  <Typography variant="body2" component="p">
                    {submissionInfo[0].body}
                  </Typography>
                  <Typography variant="body2" component="p">
                    URL ::
                    <a href={submissionInfo[0].url}>{submissionInfo[0].url}</a>
                  </Typography>
                </CardContent>
                <CardActions></CardActions>
              </Card>

              <ScoreView
                submissionId={submissionInfo[0].id}
                scores={submissionInfo[0].scores}
              />
              <br />
              <ScoreNew
                submissionId={submissionInfo[0].id}
                assignmentId={assignmentId}
                scoreTypes={submissionInfo[0].scores}
                getSubmission={getSubmission}
                memberId={memberId}
              />
            </>
          )}
        </>
      );
    }
  }
}

export default GradingView;
