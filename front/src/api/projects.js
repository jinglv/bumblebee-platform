import request from '@/utils/request'

export function projectList(params) {
  return request({
    url: '/api/projects/list',
    method: 'get',
    params
  })
}

export function createProject(data) {
  return request({
    url: '/api/projects/create',
    method: 'post',
    data
  })
}

export function getProject(id) {
  return request({
    url: '/api/projects/' + id,
    method: 'get'
  })
}
