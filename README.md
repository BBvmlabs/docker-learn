# docker-learn
Learning the Docker with all the tools using for the project in Containerized like Docker images of Nginx, Postgres, mongodb


# 1. Define the role dependency
async def get_current_master(current_user: dict = Depends(jwt_auth_dependency)):
    if not verify_master(current_user):
        raise HTTPException(status_code=403, detail="Master access required")
    return current_user

# 2. Use it in your route
@router.get('/me')
async def master_details(
    db: AsyncSession = Depends(get_db), 
    master_user: dict = Depends(get_current_master) # Now it's guaranteed to be a master
):
    # No 'if' check needed here anymore! 
    master_id = UUID(master_user.get('id'))
    # ... rest of your database logic