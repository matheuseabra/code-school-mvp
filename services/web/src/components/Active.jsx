import React from 'react'

const Active = isActive => {

    const circle = {
        width: '12px',
        marginLeft: '8px',
        height: '12px',
        borderRadius: '50%',
        background: isActive ? '#1ddb30' : '#000'
    };

    return (
        <div style={circle}></div>
    )
}

export default Active;
