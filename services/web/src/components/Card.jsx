import React from 'react';

const Card = ({ children }) => {
  return (
    <div className="demo-card-square mdl-card mdl-shadow--3dp">
      { children }
    </div>
  );
};

export default Card;
