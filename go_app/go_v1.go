package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// Create a new Gin router
	router := gin.Default()

	// Define a route to handle the "Hello, World!" message
	router.GET("/v1", func(c *gin.Context) {
		c.String(200, "Welcome to US-EAST-1A")
	})

	// Run the server on port 8080
	router.Run(":8080")
}

