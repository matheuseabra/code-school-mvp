import React from 'react';
import TabNavigator from './TabNavigator';

const Header = () => {
  const logo = "<Codr/>";
  return (
    <header className="mdl-layout__header">
      <div className="mdl-layout__header-row">
        <span className="mdl-layout-title font-sc">{logo}</span>
      </div>
      <TabNavigator/>
    </header>
  );
};

export default Header;
