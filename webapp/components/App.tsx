import React from 'react'
import { Route, Switch } from 'react-router'
import { BrowserRouter } from 'react-router-dom'

import { ExampleTodoList } from '@/components/ExampleTodoList'

export class App extends React.Component {
  public render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route
            path='/'
            exact={true}
            component={ExampleTodoList}
          />
          <Route
            render={() => <div>Page not found.</div>}
          />
        </Switch>
      </BrowserRouter>
    )
  }
}
