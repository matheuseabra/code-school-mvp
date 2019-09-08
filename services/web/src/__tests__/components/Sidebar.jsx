import React from 'react';
import { mount } from 'enzyme';

import Sidebar from '../../components/Sidebar';

test('<Sidebar />', () => {
    const wrapper = mount(<Sidebar />);
    expect(wrapper).toBeTruthy();
});