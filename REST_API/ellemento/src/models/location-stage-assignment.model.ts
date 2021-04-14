import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class LocationStageAssignment extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  location_stage_assignment_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  stage_assignment: number;

  @property({
    type: 'date',
    required: true,
  })
  validity_date_time_start: string;

  @property({
    type: 'date',
    required: true,
  })
  validity_date_time_end: string;

  @property({
    type: 'number',
    required: true,
  })
  capacity: number;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<LocationStageAssignment>) {
    super(data);
  }
}

export interface LocationStageAssignmentRelations {
  // describe navigational properties here
}

export type LocationStageAssignmentWithRelations = LocationStageAssignment & LocationStageAssignmentRelations;
