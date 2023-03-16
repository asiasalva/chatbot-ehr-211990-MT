import React from 'react'

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleDefault = async (message) => {
    console.log(message)
    fetch('http://127.0.0.1:5000/api', {
      method: 'POST',
      body: JSON.stringify({ message }),
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      crossorigin: true
    })
      .then(response => { return response.json() })
      .then(response => {
        console.log(response)
        const botMessage = createChatBotMessage(response.message)

        setState((prev) => ({
          ...prev,
          messages: [...prev.messages, botMessage]
        }))
      })
  }

  // handle multiple responses
  // Put the handleHello function in the actions object to pass to the MessageParser
  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleDefault
          }
        })
      })}
    </div>
  )
}

export default ActionProvider
