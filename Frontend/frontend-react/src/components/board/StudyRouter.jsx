import React from "react";
import { Route } from "react-router-dom";

import StudyMain from "./study/StudyMain";
import GroupDetail from "./study/GroupDetail";
import GroupNew from "./study/GroupNew";
import PostNew from "./study/PostNew";
import PostDetail from "./study/PostDetail";
import PostUpdate from "./study/PostUpdate";

function StudyRouter({ match }) {
  return (
    <>
      <Route exact path={match.path} component={StudyMain} />
      <Route exact path={`${match.path}/group/new`} component={GroupNew} />
      {/* <Route path={`${match.path}/detail/:id`} component={StudyList} id="number"/> */}

      {/* <Route
        path={`${match.path}/update/:id`}
        component={GroupUpdate}
        id="number"
      /> */}
      <Route exact path={`${match.path}/:group`} component={GroupDetail} />
      <Route path={`${match.path}/:group/post/new`} component={PostNew} />
      <Route
        path={`${match.path}/:group/detail/:id`}
        component={PostDetail}
        id="number"
      />
      <Route
        path={`${match.path}/:group/update/:id`}
        component={PostUpdate}
        id="number"
      />
    </>
  );
}

export default StudyRouter;
