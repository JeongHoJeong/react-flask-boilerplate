import React from 'react'
import styled from 'styled-components'

interface ITodo {
  id: number
  description: string
}

const Header = styled.h1`
  color: #111111;
`

const Description = styled.a`
  font-size: 18px;
  color: #111111;
  cursor: pointer;

  :hover {
    color: #0074d9;
  }
`

const DescriptionEditorForm = styled.form`
  display: inline-block;
`

const DeleteButton = styled.a`
  color: #ff4136;
  cursor: pointer;
  margin-left: 8px;
`

export class ExampleTodoList extends React.Component<TodoList.IProps, TodoList.IState> {
  public state: TodoList.IState

  constructor(props: {}) {
    super(props)

    this.state = {
      editingId: null,
      editingValue: null,
      newTodoDescription: '',
      todos: [],
    }

    this.updateItems = this.updateItems.bind(this)
  }

  public componentDidMount() {
    this.updateItems()
  }

  public render() {
    const { editingId, editingValue, newTodoDescription } = this.state

    return (
      <div>
        <Header>TODOS</Header>
        {this.state.todos.map(
          (todo) => (
            <ul key={todo.id}>
              {
                todo.id === editingId ?
                  <DescriptionEditorForm
                    onSubmit={(e) => {
                      e.preventDefault()
                      e.stopPropagation()

                      this.setState({
                        editingId: null,
                        editingValue: null,
                      })

                      fetch(`/example/todo/${todo.id}/`, {
                        body: JSON.stringify({
                          description: this.state.editingValue,
                        }),
                        headers: {
                          'Accept': 'application/json',
                          'Content-Type': 'application/json',
                        },
                        method: 'PATCH',
                      })
                        .then(() => {
                          this.updateItems()
                        })
                    }}
                  >
                    <input
                      onChange={(e) => this.setState({ editingValue: e.currentTarget.value })}
                      value={editingValue || ''}
                    />
                  </DescriptionEditorForm> :
                  <Description
                    onClick={() => {
                      this.setState({
                        editingId: todo.id,
                        editingValue: todo.description,
                      })
                    }}
                  >
                    {todo.description}
                  </Description>
              }
              <DeleteButton
                onClick={() => {
                  fetch(`/example/todo/${todo.id}/`, {
                    method: 'DELETE',
                  })
                    .then(() => {
                      this.updateItems()
                    })
                }}
              >
                Delete
              </DeleteButton>
            </ul>
          ),
        )}
        <form
          onSubmit={(e) => {
            e.preventDefault()
            e.stopPropagation()

            fetch('/example/todo/', {
              body: JSON.stringify({
                description: newTodoDescription,
              }),
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
              },
              method: 'POST',
            })
              .then(() => {
                this.updateItems()
              })

            this.setState({
              newTodoDescription: '',
            })
          }}
        >
          <div>
            <span>New todo:</span>
            <input
              value={newTodoDescription}
              onChange={(e) => this.setState({
                newTodoDescription: e.currentTarget.value,
              })}
            />
          </div>
        </form>
      </div>
    )
  }

  private updateItems() {
    fetch('/example/todos/')
      .then((data) => data.json())
      .then((json) => {
        this.setState({
          todos: json,
        })
      })
  }
}

export namespace TodoList {
  /* tslint:disable-next-line:no-empty-interface */
  export interface IProps {}
  export interface IState {
    todos: ITodo[],
    editingValue: string | null,
    editingId: number | null,
    newTodoDescription: string,
  }
}
