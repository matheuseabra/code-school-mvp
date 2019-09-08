import React from 'react';

const TabNavigator = () => {

  return (
    <div className="mdl-layout__tab-bar mdl-js-ripple-effect">
      <a href="#scroll-tab-1" className="mdl-layout__tab is-active">
        Sign Up
      </a>
      <a href="#scroll-tab-2" className="mdl-layout__tab">
        All Users
      </a>
    </div>
  );
};

export default TabNavigator;
