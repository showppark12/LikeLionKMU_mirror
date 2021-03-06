import axios from "axios";
import { tokenConfig } from "./AuthAPI";
axios.defaults.baseURL = "http://13.125.36.95/";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  /* Board CRUD api */
  //모든글 불러오기
  getAllPosts(url) {
    // console.log("getAllPosts 실행.");
    return axios.get(`board/${url}/`, tokenConfig());
  },

  //alum : 동문, 동기 -> 해당 기수의 게시물들을 불러옴.
  getMyAlumPosts(url, alum) {
    // console.log("get my alum posts API 실행.");
    return axios.get(`board/${url}/?start_number=${alum}`, tokenConfig());
  },

  //단일 글 불러오기 및 단일댓글 불러오기?
  getPost(url, id) {
    // console.log("getPost 실행");
    return axios.get(`board/${url}/` + String(id), tokenConfig());
  },

  getPage(url, id) {
    // console.log("getPage 실행");
    return axios.get(`board/${url}/?page=${id}`, tokenConfig());
  },
  getNPage(url, id) {
    // console.log("getPage 실행");
    return axios.get(`board/${url}/?page=${id}&study_type=0`, tokenConfig());
  },
  getSPage(url, id) {
    // console.log("getPage 실행");
    return axios.get(`board/${url}/?page=${id}&study_type=1`, tokenConfig());
  },

  //글 생성
  createPost(url, data) {
    // console.log(data);
    return axios.post(`board/${url}/`, data, tokenConfig());
  },

  uploadImage(data) {
    // console.log(data);
    return axios.post(`board/images/`, data, tokenConfig());
  },

  //글 수정
  updatePost(url, id, data) {
    // console.log("updatePost 실행.");
    return axios.put(`board/${url}/` + String(id) + "/", data, tokenConfig());
  },

  //글 삭제
  deletePost(url, id) {
    // console.log("deletePost 실행.");
    return axios.delete(`board/${url}/` + String(id), tokenConfig());
  },

  //댓글 불러오기
  getComments(url, id) {
    // console.log("getComments 실행.");
    return axios.get(`board/${url}/?board_id=` + String(id), tokenConfig());
  },

  //현재 like 상태 get
  getLike(url, id) {
    // console.log("get like api 실행.");
    return axios.get(`board/${url}/${id}/like/`, tokenConfig());
  },
  getUserLikePost(url) {
    // console.log("get User Liked Post 실행.");
    return axios.post(`board/${url}/user_like/`, null, tokenConfig());
  },
  //like 상태 변경요청.
  changeLike(url, id) {
    // console.log("change like status api 실행.");
    return axios.post(`board/${url}/${id}/like/`, null, tokenConfig());
  },
  getMyPost(id) {
    // console.log("get MyPost api 실행");
    return axios.get(`accounts/user/${id}/activity/`, tokenConfig());
  }
};
