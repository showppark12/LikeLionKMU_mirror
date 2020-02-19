import React, { Component } from "react";
import { Link } from "react-router-dom";
import moment from "moment";

import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import Divider from '@material-ui/core/Divider';

import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';

const useStyles = theme => ({
    root: {
        width: '100%',
        backgroundColor: theme.palette.background.paper,
      },
})

class PostView extends Component {
  render() {
    const { classes } = this.props;
    // const { id, title, body, noticeDate, authorName } = this.props;
    const { postInfo } = this.props;
    const pubDate = moment(postInfo.pub_date).format("MM-DD HH:MM");
    
    //나중에 리스트 최상위 태그 컨테이너로 뺄 것.
    return (
        <List component="nav" className={classes.root} aria-label="contacts">
            <ListItem button component={Link} to={`/notice/detail/${postInfo.id}`}>
                <ListItemAvatar>
                    <Avatar alt="Author Name" src="" />
                </ListItemAvatar>
                <ListItemText primary={postInfo.title} secondary={postInfo.author_name}/>
                <ListItemSecondaryAction>
                  <small>{pubDate}</small>
                </ListItemSecondaryAction>
            </ListItem>
            <Divider variant="inset"/>
        </List>
    );
  }
}


export default withStyles(useStyles)(PostView)