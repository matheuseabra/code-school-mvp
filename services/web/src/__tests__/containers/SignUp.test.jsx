import React from 'react';
import { mount } from 'enzyme';

import SignUp from '../../containers/SignUp';

test('<SignUp />', () => {
    const wrapper = mount(<SignUp />);
    expect(wrapper).toBeTruthy();
});