import React from 'react';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import { Link } from "react-router-dom";
import api from '../../api/api_board'
import PostView from './PostView'

class NoticeList extends React.Component {
    constructor(props){
      super(props);
      this.state = {
        noticeList : []
      };
    }
  
    componentDidMount() {
        this.getNotices()
    }
  
    async getNotices() {
        const _noticeList = await api.getAllNotices();
        console.log('getnotice 메서드 실행.');
        console.log(_noticeList);
        this.setState({noticeList : _noticeList.data});
        // console.log('postList의 타입은 : ' , typeof(this.state.postList)) 
      }

    render() {
      return (
        <div>
            <Container maxWidth="lg" className="main-container">                
                <h1>Notice List</h1>
                <h4><Link to={"/notice/new"}>New Notice</Link></h4>
                {this.state.noticeList.map((post) =>
                    (<PostView key={post.id} id={post.id} title={post.title} body={post.body} />)
                )} 
            </Container>
        </div>
      );
    }
  }
  
  
  
  export default NoticeList;