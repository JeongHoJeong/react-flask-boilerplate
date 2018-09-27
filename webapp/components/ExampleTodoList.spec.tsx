import React from 'react'
import renderer from 'react-test-renderer'

import { ExampleTodoList } from '@/components/ExampleTodoList'

describe('ExampleTodoList', () => {
  it('renders correctly', () => {
    const component = renderer.create(<ExampleTodoList />)
    const tree = component.toJSON()
    expect(tree).toMatchSnapshot()
  })
})
