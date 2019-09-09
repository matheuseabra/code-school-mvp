import React from 'react';
import { mount } from 'enzyme';

import Active from '../../components/Active';

test('<Active />', () => {
    const wrapper = mount(<Active />);
    expect(wrapper).toBeTruthy();
});