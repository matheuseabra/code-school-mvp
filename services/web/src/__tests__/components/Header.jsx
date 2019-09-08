import React from 'react';
import { mount } from 'enzyme';

import Header from '../../components/Header';

test('<Header />', () => {
    const wrapper = mount(<Header />);
    expect(wrapper).toBeTruthy();
});