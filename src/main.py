import uvicorn


def main():

    uvicorn.run(

        "app:app", 
        reload=True,
        host="localhost"
    )


if __name__ == '__main__':
    main()
