webpackJsonp([11],{0:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}var i=n(48),o=r(i),a=n(590),s=r(a),u=n(589),l=r(u);new o["default"]({ComposerHeader:s["default"]}),new o["default"]({ComposerFooter:l["default"]})},327:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}t.__esModule=!0;var i=n(163),o=r(i),a={get:function(e){var t=arguments.length<=1||void 0===arguments[1]?void 0:arguments[1];return o["default"].get("composer."+e,t)}};t["default"]=a,e.exports=t["default"]},589:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}t.__esModule=!0;var i=n(3),o=r(i),a=n(1),s=r(a),u=n(321),l=n(199),c=(r(l),n(337)),d=r(c),p=n(319),f=r(p),h=n(198),m=r(h),g=n(327),v=r(g),y=n(813),_=r(y),b=n(591),x=r(b),w=n(320),k=(r(w),s["default"].createClass({displayName:"ComposerFooter",propTypes:{course:s["default"].PropTypes.object},getInitialState:function(){var e=v["default"].get("course");e.curriculum_id=v["default"].get("curriculum_id");var t=0,n=e._id,r=o["default"](e.projects).pluck("checkpoints").flatten().value(),i=v["default"].get("course.course_exercises_index"),a=r[i-1];return{lesson:e,exercises:r,initialUnit:t,initialLesson:n,initialExercise:a,initialExerciseIndex:i,showNavigation:!1,lessonComplete:!1}},componentDidMount:function(){x["default"].on("composer:navigate",this.onComposerNavigate),x["default"].on("composer:nextProject",this.onNext),x["default"].on("composer:nextCourse",this.onNext)},onNext:function(){return this.props.segment?void this.setState({lessonComplete:!0}):window.location="/learn/"},onComposerNavigate:function(e){var t=this.state,n=t.lesson,r=t.exercises,i=o["default"].get(n.projects,"["+e.project+"].checkpoints["+e.checkpoint+"]");this.setState({initialExercise:i,initialExerciseIndex:o["default"].indexOf(r,i)+1})},getCourseNavigator:function(){var e=this.state,t=e.lesson,n=e.initialUnit,r=e.initialLesson,i=e.initialExercise;return s["default"].createElement(f["default"],{className:_["default"].modal,isOpen:this.state.showNavigation,initialUnit:n,initialLesson:r,initialExercise:i._id,titleRoute:v["default"].get("landing_path"),course:t,unlockAll:!0,onOutsideClick:this.toggleCourseNavigator})},courseIsComplete:function(){return this.props.segment&&this.isLastLesson()&&this.isLastUnit()?!0:void 0},isLastUnit:function(){return this.props.segment?this.currentUnitIndex()===this.props.segment.units.length-1:void 0},projectIsNext:function(){var e=this.currentUnit();return this.props.project?!this.isLastProject()&&e.projects.length>0:e.projects.length>0?e.projects[0].should_show?this.isLastLesson():!1:void 0},isLastLesson:function(){var e=this.currentUnit();return 0===e.lessons.length?!0:this.currentLessonIndex()===e.lessons.length-1?!0:!1},currentLesson:function(){return this.props.segment?this.props.segment.lessons[this.currentLessonIndex()]:void 0},currentLessonIndex:function C(){var e=this.currentUnit(),C=void 0,t=this.state.lesson.name;return e.lessons.forEach(function(e,n){e.title===t&&(C=n)}),C},currentUnit:function(){return this.props.segment?this.props.segment.units[this.currentUnitIndex()]:void 0},currentUnitIndex:function M(){var e=this.props.segment,t=e.units,n=this.state.lesson.name,M=void 0;return t.forEach(function(e,t){e.lessons.forEach(function(e){e.title===n&&(M=t)})}),M},completeLesson:function(){var e=void 0,t=void 0,n=this.currentUnit();if(this.courseIsComplete())return void(window.location=v["default"].get("landing_path"));if(this.projectIsNext())e=n.projects[0];else if(this.isLastLesson()){var r=this.currentUnitIndex(),i=this.props.segment.units[r+1];if(t=i.lessons[0],!t&&(e=i.projects[0],!e.should_show))return void(window.location=v["default"].get("landing_path"))}else t=n.lessons[this.currentLessonIndex()+1];return s["default"].createElement(m["default"],{type:"screen",course:this.state.lesson,nextProject:e,onClose:this.clearWall,nextLesson:t})},toggleCourseNavigator:function(){this.setState({showNavigation:!this.state.showNavigation})},render:function(){this.currentUnit();var e=this.state.initialExercise,t=void 0;return e&&(t=this.state.initialExerciseIndex+". "+e.name),s["default"].createElement(u.Footer,{className:_["default"].footer},s["default"].createElement(u.FooterSection,{position:"left"},s["default"].createElement(u.FooterTab,null,s["default"].createElement(d["default"],{title:t,"data-cue":"course-navigator",onClick:this.toggleCourseNavigator,active:this.state.showNavigation}))),this.getCourseNavigator(),this.state.lessonComplete&&this.props.segment?this.completeLesson():void 0)}}));t["default"]=k,e.exports=t["default"]},590:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}t.__esModule=!0;var i=n(1),o=r(i),a=n(325),s=n(327),u=r(s),l=n(20),c=r(l),d=n(814),p=r(d),f=o["default"].createClass({displayName:"ComposerHeader",propTypes:{},render:function(){var e=u["default"].get("curriculum_title")||u["default"].get("course.name");return o["default"].createElement(a.Header,{"data-react-composer-header":!0,className:p["default"].header,title:e,titleRoute:u["default"].get("landing_path"),profileImage:c["default"].get("profile_image_url")})}});t["default"]=f,e.exports=t["default"]},591:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}t.__esModule=!0;var i=n(3),o=r(i),a=n(371),s=r(a),u={};o["default"].extend(u,s["default"].Events),window.ComposerEvents=u,t["default"]=u,e.exports=t["default"]},813:function(e,t){e.exports={footer:"index__footer___2qYaX",navButton:"index__navButton___3Q91y",modal:"index__modal___2ZkMt"}},814:function(e,t){e.exports={header:"index__header___2fkD3"}}});